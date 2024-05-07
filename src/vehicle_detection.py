import cv2
import torch
import torchvision.models as models

model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

def detect_vehicles(frames):
    """Detecta veículos em frames de vídeo."""
    results = []
    for frame in frames:
        with torch.no_grad():
            pred = model([torch.from_numpy(frame).permute(2, 0, 1).float().cuda()])
        results.append(pred)
    return results
