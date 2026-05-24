const API_BASE = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000/api";

export type PlayerCard = {
  id: string;
  full_name: string;
  photo_url: string | null;
  goals_scored: number;
  games_played: number;
  successful_tackles: number;
  successful_passes: number;
};

export async function subscribe(phone_e164: string, display_name?: string) {
  const response = await fetch(`${API_BASE}/subscriptions`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ phone_e164, display_name: display_name || null }),
  });
  if (!response.ok) {
    throw new Error("Failed to subscribe");
  }
  return response.json();
}

export async function unsubscribe(phone_e164: string) {
  const response = await fetch(`${API_BASE}/subscriptions/unsubscribe`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ phone_e164 }),
  });
  if (!response.ok) {
    throw new Error("Failed to unsubscribe");
  }
  return response.json();
}

export async function fetchActivePlayers(): Promise<PlayerCard[]> {
  const response = await fetch(`${API_BASE}/players/active`);
  if (!response.ok) {
    throw new Error("Failed to load players");
  }
  return response.json();
}
