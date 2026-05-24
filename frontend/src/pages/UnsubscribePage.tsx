import { FormEvent, useState } from "react";

import { unsubscribe } from "../lib/api";

export function UnsubscribePage() {
  const [phone, setPhone] = useState("");
  const [status, setStatus] = useState<string | null>(null);

  async function onSubmit(event: FormEvent) {
    event.preventDefault();
    setStatus(null);
    try {
      const result = await unsubscribe(phone);
      setStatus(`Subscription status: ${result.whatsapp_status}`);
    } catch {
      setStatus("Unsubscribe failed");
    }
  }

  return (
    <section className="panel">
      <h2>Unsubscribe</h2>
      <form onSubmit={onSubmit}>
        <input
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
          placeholder="Phone in E.164 format (e.g. +9725XXXXXXXX)"
          required
        />
        <button type="submit">Unsubscribe</button>
      </form>
      {status && <p className="muted">{status}</p>}
    </section>
  );
}
