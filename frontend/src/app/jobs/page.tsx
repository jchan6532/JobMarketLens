import JobCard from '@/components/jobs/JobCard';
import { JobSummary } from '@/types/JobSummary';

const MOCK: JobSummary[] = [
  {
    id: 1,
    title: 'Backend Engineer',
    company: 'Acme',
    city: 'Toronto',
    province: 'ON',
    country: 'Canada',
    posted_date: '2025-12-21',
    role_category: 'backend',
    skills: [
      { slug: 'python', name: 'Python', category: 'language' },
      { slug: 'fastapi', name: 'FastAPI', category: 'backend' },
      { slug: 'postgresql', name: 'PostgreSQL', category: 'database' },
    ],
  },
];

export default function JobsPage() {
  return (
    <main className='mx-auto max-w-3xl p-6'>
      <h1 className='text-xl font-semibold'>Jobs</h1>
      <div className='mt-4 space-y-3'>
        {MOCK.map((j) => (
          <JobCard key={j.id} job={j} />
        ))}
      </div>
    </main>
  );
}
