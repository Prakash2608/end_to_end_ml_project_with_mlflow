from mlProject2.config.configuration import ConfigurationManager
from mlProject2.components.model_evaluation import ModelEvaluation
from mlProject2 import logger


STAGE_NAME = "Model Evalaution stage"

class ModelEvalautionTrainingPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config = model_evaluation_config)
        model_evaluation_config.log_into_mlflow()
        
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_evaluation = ModelEvalautionTrainingPipeline()
        model_evaluation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        
    except Exception as e:
        logger.exception(e)
        raise e