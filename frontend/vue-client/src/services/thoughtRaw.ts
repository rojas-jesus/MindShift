import api from './auth';

export interface ThoughtRawEntry {
  id: number;
  transcription: string;
  timestamp: string;
}

export const thoughtRawService = {
  async createThoughtRaw(transcription: string): Promise<ThoughtRawEntry> {
    console.log('THOUGHT_RAW_TRACE: Attempting to save thought to api/thought-raw/create/');
    try {
      const response = await api.post('api/thought-raw/create/', {
        transcription,
      });
      console.log('THOUGHT_RAW_TRACE: Success!', response.status);
      return response.data;
    } catch (error: any) {
      console.error('THOUGHT_RAW_TRACE: Failed!', error.response?.status, error.message);
      throw error;
    }
  },
};
