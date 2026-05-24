import { Link, Route, Routes } from "react-router-dom";

import { AdminPage } from "./pages/AdminPage";
import { LandingPage } from "./pages/LandingPage";
import { PlayersPage } from "./pages/PlayersPage";
import { SubscribePage } from "./pages/SubscribePage";
import { UnsubscribePage } from "./pages/UnsubscribePage";

export function App() {
  return (
    <div className="layout">
      <header className="header">
        <h1>Maccabi Fan Platform</h1>
        <nav>
          <Link to="/">Home</Link>
          <Link to="/subscribe">Subscribe</Link>
          <Link to="/unsubscribe">Unsubscribe</Link>
          <Link to="/players">Players</Link>
          <Link to="/admin">Admin</Link>
        </nav>
      </header>

      <main className="content">
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/subscribe" element={<SubscribePage />} />
          <Route path="/unsubscribe" element={<UnsubscribePage />} />
          <Route path="/players" element={<PlayersPage />} />
          <Route path="/admin" element={<AdminPage />} />
        </Routes>
      </main>
    </div>
  );
}
