type Props = {
  params: { id: string };
};

export default function JobDetailPage({ params }: Props) {
  return <div>Job ID: {params.id}</div>;
}
