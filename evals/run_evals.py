from dataclasses import dataclass

from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import Evaluator, EvaluatorContext

from app.ai.decide import decide
from app.ai.schemas import Decision
from evals.golden_emails import GOLDEN_EMAILS

Expected = dict[str, str]


@dataclass
class SectionMatches(Evaluator[str, Decision, Expected]):
    def evaluate(self, ctx: EvaluatorContext[str, Decision, Expected]) -> bool:
        if ctx.metadata is None:
            return False
        return ctx.output.section == ctx.metadata["section"]


@dataclass
class ActionMatches(Evaluator[str, Decision, Expected]):
    def evaluate(self, ctx: EvaluatorContext[str, Decision, Expected]) -> bool:
        if ctx.metadata is None:
            return False
        return ctx.output.action == ctx.metadata["action"]


def run_pipeline(email: str) -> Decision:
    return decide(email)


dataset: Dataset[str, Decision, Expected] = Dataset(
    name="golden-emails",
    cases=[
        Case(
            name=case["name"],
            inputs=case["email"],
            metadata={"section": case["section"], "action": case["action"]},
        )
        for case in GOLDEN_EMAILS
    ],
    evaluators=[SectionMatches(), ActionMatches()],
)

if __name__ == "__main__":
    report = dataset.evaluate_sync(run_pipeline, max_concurrency=4)
    report.print(include_input=False, include_output=True, include_durations=False)