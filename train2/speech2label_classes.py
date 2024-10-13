import os
import json
import torch
import torch.nn as nn
from torch.utils.data import Dataset

input_dim = 128  # Размерность MFCC


# --- Датасет ---
class SpeechDataset(Dataset):
    def __init__(self, audio_folder, json_file, transform=None):
        with open(json_file, "r", encoding="utf-8") as f:
            self.data = json.load(f)
        self.audio_folder = audio_folder
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        audio_path = os.path.join(self.audio_folder, self.data[idx]["audio_filepath"])
        text = self.data[idx].get("text", "")
        mfcc = self.transform(audio_path) if self.transform else audio_path
        if mfcc is None:
            print(f"Error loading MFCC for audio: {audio_path}")
            mfcc = torch.zeros((1, input_dim))
        return torch.tensor(mfcc, dtype=torch.float32), text


# --- Модель с LSTM ---
class LSTMSpeechRecognizer(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.lstm = nn.LSTM(
            input_dim, hidden_dim, batch_first=True, bidirectional=True
        )  # Двунаправленный LSTM
        self.fc1 = nn.Linear(
            hidden_dim * 2, hidden_dim
        )  # Увеличение размерности входного слоя
        self.fc2 = nn.Linear(hidden_dim, output_dim)  # Полносвязный слой для вывода
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        x, _ = self.lstm(x)  # Получение выходных данных LSTM
        x = x.mean(dim=1)  # Среднее по временной оси
        x = self.fc1(x)
        x = nn.ReLU()(x)
        x = self.dropout(x)
        x = self.fc2(x)
        return x
