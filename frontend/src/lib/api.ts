import axios from 'axios';

const API_BASE =
  process.env.NEXT_PUBLIC_API_BASE_URL ?? 'http://127.0.0.1:8000';

const api = axios.create({
  baseURL: API_BASE,
  // matches fetch(cache: 'no-store') behavior in dev
  headers: {
    'Cache-Control': 'no-store',
  },
});

export async function apiGet<T>(path: string): Promise<T> {
  try {
    const res = await api.get<T>(path);
    return res.data;
  } catch (err: any) {
    if (err.response) {
      throw new Error(`API error ${err.response.status} on GET ${path}`);
    }
    throw err;
  }
}
