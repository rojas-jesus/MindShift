import api from './auth';

export interface VoiceThoughtEntry {
  id: number;
  transcription: string;
  timestamp: string;
}

export const voiceThoughtService = {
  async createVoiceThought(transcription: string): Promise<VoiceThoughtEntry> {
    const response = await api.post('/api/voice/thought/create/', {
      transcription,
    });
    return response.data;
  },
};

