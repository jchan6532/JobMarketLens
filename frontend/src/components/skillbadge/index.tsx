type Props = {
  name: string;
};

export default function SkillBadge({ name }: Props) {
  return <span className='rounded-full border px-3 py-1 text-sm'>{name}</span>;
}
