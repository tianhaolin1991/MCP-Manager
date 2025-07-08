import dspy
from process.llm import call_lm, LLMCallRecord
from cons.constants import *
import logging

EVALUATE_PROMPT = """对于以下问题：{question}

请判断预测答案是否回答正确，回答对关键信息就算正确:

预测答案: {prediction}
正确答案: {ground_truth}

只需要返回True或False。"""

class Evaluator:

    @staticmethod
    def evaluate_final_answer(
                question: str,
                ground_truth: str,
                prediction: str,
                record: LLMCallRecord,
                logger: logging.Logger,
                ) -> bool: # Modified return type to bool
        prompt = EVALUATE_PROMPT.format(question=question, prediction=prediction, ground_truth=ground_truth)
        messages = [
            {
                ROLE: Role.USER,
                CONTENT: prompt
            }
        ]
        logger.info(f"开始评测final answer")
        logger.info(f"question: {question}")
        logger.info(f"ground_truth: {ground_truth}")
        logger.info(f"prediction: {prediction}")

        # Create a temporary manager for the judge model
        judge_manager = LLMCallRecord(
            id=f"{record.id}_judge", # Append _judge to the original ID
            lm_api_key=manager.lm_api_key,
            lm_api_base=manager.lm_api_base,
            model="deepseek-v3-250324", # Specify the fixed judge model here
            lm_usages=[], # Start with empty usage for this call
            mcp_rts=[],
            mcp_retry_times=[]
        )

        response_content, _, _ = call_lm(messages, judge_manager, logger, temperature=0.01)

        # Optionally, you might want to aggregate the judge_manager's usage back to the original manager
        # manager.lm_usages.extend(judge_manager.lm_usages)

        return "true" in response_content.lower()

    @staticmethod
    def question_scorer(
            question: str, # Add question parameter
            model_answer: str,
            ground_truth: str,
            record: LLMCallRecord, # Add manager parameter
            logger: logging.Logger
    ) -> bool:
        # Use LM for evaluation
        logger.info("Using LM for final answer evaluation.")
        is_correct = Evaluator.evaluate_final_answer(question, ground_truth, model_answer, manager, logger) # Use model_answer as prediction
        return is_correct # Return the boolean result

def mcp_metric(example: dspy.Example, pred: dspy.Prediction):
    return pred.success

if __name__ == "__main__":
    print(Evaluator.question_scorer("100+23=?", "123", "123"))
    