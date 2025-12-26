import Link from 'next/link';
import { JobSummary } from '@/types/JobSummary';

type Props = {
  job: JobSummary;
  href?: string;
  showSkills?: boolean;
  maxSkills?: number;
};

function formatLocation(job: JobSummary) {
  const city = (job.city ?? '').trim();
  const prov = (job.province ?? '').trim();

  if (city && prov) return `${city}, ${prov}`;
  if (city) return city;
  if (prov) return prov;
  return (job.country ?? 'Canada').trim() || 'Canada';
}

function formatDate(iso?: string | null) {
  if (!iso) return null;
  // ISO date like "2025-12-21"
  return iso;
}

export default function JobCard({
  job,
  href,
  showSkills = true,
  maxSkills = 6,
}: Props) {
  const to = href ?? `/jobs/${job.id}`;
  const location = formatLocation(job);
  const posted = formatDate(job.posted_date);

  const skills = (job.skills ?? []).slice(0, maxSkills);

  return (
    <Link
      href={to}
      className='block rounded-xl border border-neutral-200 bg-white p-4 shadow-sm transition hover:shadow-md'
    >
      <div className='flex items-start justify-between gap-3'>
        <div className='min-w-0'>
          <h3 className='truncate text-base font-semibold text-neutral-900'>
            {job.title}
          </h3>

          <div className='mt-1 text-sm text-neutral-600'>
            <span className='font-medium text-neutral-700'>
              {(job.company ?? '').trim() || 'Unknown company'}
            </span>
            {' • '}
            <span>{location}</span>
            {posted ? (
              <>
                {' • '}
                <span>Posted {posted}</span>
              </>
            ) : null}
          </div>
        </div>

        {job.role_category ? (
          <span className='shrink-0 rounded-full border border-neutral-200 px-2 py-1 text-xs text-neutral-700'>
            {job.role_category}
          </span>
        ) : null}
      </div>

      {showSkills && skills.length > 0 ? (
        <div className='mt-3 flex flex-wrap gap-2'>
          {skills.map((s) => (
            <span
              key={s.slug}
              className='rounded-full bg-neutral-100 px-2 py-1 text-xs text-neutral-800'
              title={s.category ?? undefined}
            >
              {s.name}
            </span>
          ))}
        </div>
      ) : null}
    </Link>
  );
}
