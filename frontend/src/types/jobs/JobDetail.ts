import { JobSkill } from './JobSkill';

export type JobDetail = {
  id: number;
  title: string;
  company?: string | null;
  city?: string | null;
  province?: string | null;
  country?: string | null;
  posted_date?: string | null; // ISO string
  role_category?: string | null;
  description?: string | null;
  skills: JobSkill[];
};
