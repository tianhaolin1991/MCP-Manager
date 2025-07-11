import dspy
from process.llm import LLMCallRecord, LLM
from cons.constants import *
import logging

EVALUATE_PROMPT = """对于以下问题：{question}

请判断预测答案是否回答正确，回答对关键信息就算正确:

预测答案: {prediction}
正确答案: {ground_truth}

只需要返回True或False。"""


class Evaluator:

    @staticmethod
    def evaluate_final_answer(llm:LLM,
            question: str,
            ground_truth: str,
            prediction: str,
            record: LLMCallRecord,
            logger: logging.Logger,
    ) -> bool:  # Modified return type to bool
        prompt = EVALUATE_PROMPT.format(question=question, prediction=prediction, ground_truth=ground_truth)
        messages = [
            {
                ROLE: Role.USER,
                CONTENT: prompt
            }
        ]
        logger.info(f"""[EVALUATE]
{{
    question: {question},
    ground truth: {ground_truth},
    prediction: {prediction}
}}
[/EVALUATE]""")

        # Create a temporary manager for the judge model
        judge_record = LLMCallRecord(
            id=f"{record.id}_judge",  # Append _judge to the original ID
            lm_usages=[],  # Start with empty usage for this call
            mcp_rts=[],
            mcp_retry_times=[]
        )

        response_content, _, _ = llm.call(messages, judge_record, temperature=0.01, logger=logger)

        # Optionally, you might want to aggregate the judge_manager's usage back to the original manager
        # manager.lm_usages.extend(judge_manager.lm_usages)

        return "true" in response_content.lower()

    @staticmethod
    def question_scorer(llm,
            question: str,  # Add question parameter
            model_answer: str,
            ground_truth: str,
            record: LLMCallRecord,  # Add manager parameter
            logger: logging.Logger
    ) -> bool:
        # Use LM for evaluation
        is_correct = Evaluator.evaluate_final_answer(llm, question, ground_truth, model_answer, record, logger)  # Use model_answer as prediction
        return is_correct  # Return the boolean result

    @staticmethod
    def mcp_metric(example:dspy.Example, pred: dspy.Prediction):
        return pred.success

