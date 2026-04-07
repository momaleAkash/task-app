import { useTasks } from "../hooks/useTasks";

export default function Tasks() {
  const { data, isLoading, error } = useTasks();

  if (isLoading) return <p className="p-4">Loading...</p>;
  if (error) return <p className="p-4 text-red-500">Error loading tasks</p>;

  return (
    <div className="max-w-2xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Task Manager</h1>

      {data.map((task) => (
        <div
          key={task.id}
          className="border rounded-lg p-4 mb-3 shadow-sm hover:shadow-md transition"
        >
          <h2 className="font-semibold text-lg">{task.title}</h2>
          <p className="text-gray-600">{task.description}</p>
        </div>
      ))}
    </div>
  );
}