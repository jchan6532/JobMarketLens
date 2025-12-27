import { apiGet } from '@/lib/api';
import type { JobDetail } from '@/types/jobs/JobDetail';
import SkillBadge from '@/components/skillbadge';

type Props = {
  params: Promise<{ id: string }>;
};

function formatLocation(job: JobDetail): string {
  const parts = [job.city, job.province, job.country].filter(Boolean);
  return parts.length ? parts.join(', ') : 'Location not provided';
}

export default async function JobDetailPage({ params }: Props) {
  const { id } = await params;
  const jobId = Number(id);

  if (!Number.isFinite(jobId)) {
    return (
      <div className='p-6'>
        <h1 className='text-xl font-semibold'>Invalid job id</h1>
      </div>
    );
  }

  // Adjust endpoint if yours differs (example: /jobs/{id})
  const job = await apiGet<JobDetail>(`/jobs/${jobId}`);

  return (
    <main className='mx-auto max-w-4xl p-6'>
      <div className='rounded-xl border p-6 shadow-sm'>
        <h1 className='text-2xl font-bold'>{job.title}</h1>

        <div className='mt-2 space-y-1 text-sm text-neutral-600'>
          <div>
            <span className='font-medium text-neutral-900'>Company:</span>{' '}
            {job.company || 'Not provided'}
          </div>

          <div>
            <span className='font-medium text-neutral-900'>Location:</span>{' '}
            {formatLocation(job)}
          </div>

          <div>
            <span className='font-medium text-neutral-900'>Role category:</span>{' '}
            {job.role_category || 'Not classified'}
          </div>

          <div>
            <span className='font-medium text-neutral-900'>Posted:</span>{' '}
            {job.posted_date
              ? new Date(job.posted_date).toLocaleDateString()
              : 'Unknown'}
          </div>
        </div>

        <hr className='my-6' />

        <h2 className='text-lg font-semibold'>Skills</h2>
        {job.skills?.length ? (
          <div className='mt-3 flex flex-wrap gap-2'>
            {job.skills.map((s) => (
              <SkillBadge key={s.slug} name={s.name} />
            ))}
          </div>
        ) : (
          <p className='mt-2 text-sm text-neutral-600'>No extracted skills.</p>
        )}

        <hr className='my-6' />

        <h2 className='text-lg font-semibold'>Description</h2>
        <div className='mt-3 whitespace-pre-wrap text-sm leading-6 text-neutral-800'>
          {job.description || 'No description provided.'}
        </div>
      </div>
    </main>
  );
}
