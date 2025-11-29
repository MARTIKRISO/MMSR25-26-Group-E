import torch


class RandomBaselineModule(torch.nn.Module):
    def __init__(self,
                 lower_bound_score: float = 0.0,
                 upper_bound_score: float = 1.0):
        super(RandomBaselineModule, self).__init__()
        self.register_buffer(name='_lower_bound_score',
                             tensor=torch.tensor(lower_bound_score),
                             persistent=True)
        self.register_buffer(name='_upper_bound_score',
                             tensor=torch.tensor(upper_bound_score),
                             persistent=True)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        rand = torch.rand_like(input=x,
                               dtype=torch.float64)
        return self._lower_bound_score + rand * (self._upper_bound_score - self._lower_bound_score)

    @torch.jit.ignore
    def is_scripted(self) -> bool:
        return isinstance(self, torch.jit.ScriptModule)

    @torch.jit.ignore
    def save_as_scripted(self, path: str) -> None:
        scripted = self
        if not self.is_scripted():
            scripted = torch.jit.script(scripted)
        scripted.save(path)



if __name__ == '__main__':
    base_model = RandomBaselineModule(lower_bound_score=0.0,
                                      upper_bound_score=1.0)

    base_model.save_as_scripted('../../modules/random_baseline_module.pt')
    base_model = torch.jit.script(base_model)


    def test_batch(batch_size: int):
        spotify_ids = [f'spotify_id_{i}' for i in range(batch_size)]
        print(f'\nBatch size: {batch_size}')
        print(f'Example IDs:\n {spotify_ids}')

        dummy_input = torch.zeros(batch_size, dtype=torch.float64)

        output = base_model(dummy_input)
        print(f'Model output shape: {output.shape}')
        print(f'Model output: {output}')

    for bs in [1, 32, 64, 128]:
        print('='*100)
        test_batch(bs)
