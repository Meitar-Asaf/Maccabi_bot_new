import { useEffect, useState } from "react";

import { PlayerCard, fetchActivePlayers } from "../lib/api";

export function PlayersPage() {
  const [players, setPlayers] = useState<PlayerCard[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchActivePlayers().then(setPlayers).catch(() => setError("Failed to load active players"));
  }, []);

  return (
    <section className="panel">
      <h2>Active Player Statistics</h2>
      {error && <p>{error}</p>}
      <div className="grid">
        {players.map((player) => (
          <article className="panel player-card" key={player.id}>
            {player.photo_url && <img src={player.photo_url} alt={player.full_name} />}
            <h3>{player.full_name}</h3>
            <p>Goals scored: {player.goals_scored}</p>
            <p>Games played: {player.games_played}</p>
            <p>Successful tackles: {player.successful_tackles}</p>
            <p>Successful passes: {player.successful_passes}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
