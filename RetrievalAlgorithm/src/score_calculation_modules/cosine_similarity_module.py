import torch
from torch.nn.functional import cosine_similarity


class CosineSimilarityModule(torch.nn.Module):
    def __init__(self):
        super(CosineSimilarityModule, self).__init__()

    def forward(self,
                query_track: torch.Tensor,
                target_track: torch.Tensor
        ) -> torch.Tensor:
        sim = cosine_similarity(query_track, target_track, dim=-1)
        # sim.size() = (B,1)
        return sim.unsqueeze(-1)

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
    unimodal_model = CosineSimilarityModule()
    unimodal_model.save_as_scripted('../../modules/cosine_similarity_module.pt')
    unimodal_model = torch.jit.script(unimodal_model)

    # Single input (D,)
    q_single = torch.randn(512)
    t_single = torch.randn(512)
    sim_single = unimodal_model(q_single, t_single)
    print('Single input similarity:', sim_single)
    print('Output size', sim_single.size())

    # Batch input (B, D)
    q_batch = torch.randn(4, 512)
    t_batch = torch.randn(4, 512)
    sim_batch = unimodal_model(q_batch, t_batch)
    print('Batch input similarity:', sim_batch)
    print('Output size', sim_batch.size())