import logging
import joblib
from pathlib import Path
from backend.config import MODEL_HCM_PATH, MODEL_HANOI_PATH

logger = logging.getLogger("uvicorn.error")

class ModelService:
    def __init__(self):
        self.model_hcm = None
        self.model_hanoi = None
        self.path_hcm = MODEL_HCM_PATH
        self.path_hanoi = MODEL_HANOI_PATH

    def load_model(self):
        if not self.path_hcm.exists() or not self.path_hanoi.exists():
            error_msg = f"Model files not found. Ensure both {self.path_hcm} and {self.path_hanoi} exist."
            logger.error(error_msg)
            raise FileNotFoundError(error_msg)

        logger.info(f"Loading ML models from {self.path_hcm} and {self.path_hanoi}...")
        self.model_hcm = joblib.load(self.path_hcm)
        self.model_hanoi = joblib.load(self.path_hanoi)
        logger.info("ML models loaded successfully into memory.")

    def get_model(self, province: str):
        if self.model_hcm is None or self.model_hanoi is None:
            self.load_model()
        if "Hồ Chí Minh" in province:
            return self.model_hcm
        else:
            return self.model_hanoi

    def get_model_info(self):
        return {
            "model_name": "Multiple Linear Regression",
            "algorithm": "sklearn.linear_model.LinearRegression",
            "model_path": f"HCM: {self.path_hcm}, Hanoi: {self.path_hanoi}",
            "test_metrics": {
                "raw": {
                    "r2": 0.3729,
                    "mae_million_vnd": 8417.93,
                    "rmse_million_vnd": 21435.74
                },
                "clipped": {
                    "r2": 0.3839,
                    "mae_million_vnd": 8065.00,
                    "rmse_million_vnd": 21247.69
                }
            },
            "test_samples": 9172,
            "total_features": 280,
            "numerical_features": [
                "area_m2", "log_area", "area_sq", "bedrooms",
                "frontage", "distance_to_center_km", "log_distance", "area_dist_inter"
            ],
            "categorical_features": ["province", "district"],
            "target_unit": "Million VND (Triệu VNĐ)"
        }

model_service = ModelService()
