import { BrowserRouter, Routes, Route } from 'react-router-dom';
import EventList from './pages/EventList';
import EventDetail from './pages/EventDetail';
import CreateEvent from './pages/CreateEvent';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<EventList />} />
        <Route path="/events/:id" element={<EventDetail />} />
        <Route path="/create" element={<CreateEvent />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
