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

  async getAllThoughtRaw(): Promise<ThoughtRawEntry[]> {
    console.log('THOUGHT_RAW_TRACE: Fetching all raw thoughts');
    try {
      const response = await api.get('api/thought-raw/');
      console.log('THOUGHT_RAW_TRACE: Fetched', response.data.length, 'thoughts');
      return response.data;
    } catch (error: any) {
      console.error('THOUGHT_RAW_TRACE: Fetch failed!', error.response?.status, error.message);
      throw error;
    }
  },

  async updateThoughtRaw(id: number, transcription: string): Promise<ThoughtRawEntry> {
    console.log('THOUGHT_RAW_TRACE: Updating thought', id);
    try {
      const response = await api.put(`api/thought-raw/${id}/`, {
        transcription,
      });
      console.log('THOUGHT_RAW_TRACE: Update success!');
      return response.data;
    } catch (error: any) {
      console.error('THOUGHT_RAW_TRACE: Update failed!', error.response?.status, error.message);
      throw error;
    }
  },

  async deleteThoughtRaw(id: number): Promise<void> {
    console.log('THOUGHT_RAW_TRACE: Deleting thought', id);
    try {
      await api.delete(`api/thought-raw/${id}/`);
      console.log('THOUGHT_RAW_TRACE: Delete success!');
    } catch (error: any) {
      console.error('THOUGHT_RAW_TRACE: Delete failed!', error.response?.status, error.message);
      throw error;
    }
  },
};
