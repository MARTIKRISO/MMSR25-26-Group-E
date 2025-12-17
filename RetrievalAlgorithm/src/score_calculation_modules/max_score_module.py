import torch


class MaxScoreModule(torch.nn.Module):
    def __init__(self):
        super(MaxScoreModule, self).__init__()

    def forward(self, scores: torch.Tensor) -> torch.Tensor:
        return  scores.max(dim=-1)[0]

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
    torch.manual_seed(16)
    max_score_module = MaxScoreModule()
    max_score_module.eval()
    max_score_module.save_as_scripted('../../modules/max_score_module.pt')
    max_score_module = torch.jit.script(max_score_module)

    # Single input (D,)
    dummy_scores_single_sample = torch.tensor([0.3, 0.4, 0.5])
    score_single = max_score_module(dummy_scores_single_sample)
    print('Single input similarity:', score_single)
    print('Output size', score_single.size())

    # Batch input (B, D)
    dummy_scores_batch = torch.tensor([[0.3, 0.4, 0.5],
                                      [0.6, 0.7, 0.3],
                                      [0.5, 0.1, 0.4]])
    score_batch = max_score_module(dummy_scores_batch)
    print('Batch input similarity:', score_batch)
    print('Output size', score_batch.size())
