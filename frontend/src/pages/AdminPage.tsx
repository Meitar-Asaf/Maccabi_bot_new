import { useEffect, useState } from "react";

type SubscriberSummary = { active: number; pending_opt_in: number; unsubscribed: number };
type JobSummary = { queued: number; processing: number; failed: number; sent: number };

const API_BASE = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000/api";

export function AdminPage() {
  const [subscribers, setSubscribers] = useState<SubscriberSummary | null>(null);
  const [jobs, setJobs] = useState<JobSummary | null>(null);

  useEffect(() => {
    fetch(`${API_BASE}/admin/subscribers/summary`)
      .then((r) => r.json())
      .then(setSubscribers)
      .catch(() => undefined);

    fetch(`${API_BASE}/admin/notifications/jobs`)
      .then((r) => r.json())
      .then(setJobs)
      .catch(() => undefined);
  }, []);

  return (
    <section className="panel">
      <h2>Admin Dashboard</h2>
      <p className="muted">Supabase Auth integration is the next step for protecting this page.</p>

      <div className="panel">
        <h3>Subscribers</h3>
        <p>Active: {subscribers?.active ?? "-"}</p>
        <p>Pending Opt-in: {subscribers?.pending_opt_in ?? "-"}</p>
        <p>Unsubscribed: {subscribers?.unsubscribed ?? "-"}</p>
      </div>

      <div className="panel">
        <h3>Notification Jobs</h3>
        <p>Queued: {jobs?.queued ?? "-"}</p>
        <p>Processing: {jobs?.processing ?? "-"}</p>
        <p>Failed: {jobs?.failed ?? "-"}</p>
        <p>Sent/Completed: {jobs?.sent ?? "-"}</p>
      </div>
    </section>
  );
}
