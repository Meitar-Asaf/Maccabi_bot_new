import { FormEvent, useState } from "react";

import { subscribe } from "../lib/api";

export function SubscribePage() {
  const [phone, setPhone] = useState("");
  const [name, setName] = useState("");
  const [status, setStatus] = useState<string | null>(null);

  async function onSubmit(event: FormEvent) {
    event.preventDefault();
    setStatus(null);
    try {
      const result = await subscribe(phone, name);
      setStatus(`Subscription status: ${result.whatsapp_status}`);
    } catch {
      setStatus("Subscription failed");
    }
  }

  return (
    <section className="panel">
      <h2>Subscribe</h2>
      <form onSubmit={onSubmit}>
        <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Name (optional)" />
        <input
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
          placeholder="Phone in E.164 format (e.g. +9725XXXXXXXX)"
          required
        />
        <button type="submit">Subscribe</button>
      </form>
      {status && <p className="muted">{status}</p>}
    </section>
  );
}
