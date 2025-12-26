export type JobSummary = {
  id: number;
  title: string;
  company?: string | null;
  city?: string | null;
  province?: string | null;
  country?: string | null;
  posted_date?: string | null; // ISO date string
  role_category?: string | null;
  skills?: { slug: string; name: string; category?: string | null }[]; // optional
};
