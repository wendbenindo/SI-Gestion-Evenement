import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { getEvents } from '../services/api';

function EventList() {
  const [events, setEvents] = useState([]);
  const [search, setSearch] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadEvents();
  }, [search]);

  // Recharger quand on revient sur la page
  useEffect(() => {
    const handleFocus = () => {
      loadEvents();
    };
    
    window.addEventListener('focus', handleFocus);
    return () => window.removeEventListener('focus', handleFocus);
  }, []);

  const loadEvents = async () => {
    try {
      setLoading(true);
      const data = await getEvents(search);
      
      // Récupérer le nombre d'inscriptions pour chaque événement
      const eventsWithCounts = await Promise.all(
        data.map(async (event) => {
          try {
            const registrations = await getEventRegistrations(event.id);
            return { ...event, registrations_count: registrations.length };
          } catch {
            return { ...event, registrations_count: 0 };
          }
        })
      );
      
      setEvents(eventsWithCounts);
    } catch (error) {
      console.error('Erreur:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-4xl mx-auto px-4 py-8">
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-3xl font-bold">Événements</h1>
          <Link
            to="/create"
            className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 font-semibold"
          >
            + Créer un événement
          </Link>
        </div>
        
        <input
          type="text"
          placeholder="Rechercher un événement..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full px-4 py-2 border rounded-lg mb-6"
        />

        {loading ? (
          <p>Chargement...</p>
        ) : (
          <div className="space-y-4">
            {events.map((event) => {
              const placesRestantes = event.capacity - (event.registrations_count || 0);
              const isComplet = placesRestantes === 0;

              return (
                <Link
                  key={event.id}
                  to={`/events/${event.id}`}
                  className={`block p-4 border rounded-lg hover:shadow-md transition ${
                    isComplet ? 'bg-red-50 border-red-200' : 'bg-white hover:border-blue-300'
                  }`}
                >
                  <h2 className="text-xl font-semibold text-gray-800">{event.title}</h2>
                  <p className="text-gray-600 mt-1">{new Date(event.date).toLocaleDateString('fr-FR')}</p>
                  <p className="text-gray-600">{event.location}</p>
                  <p className={`mt-2 font-semibold ${isComplet ? 'text-red-600' : 'text-green-600'}`}>
                    {isComplet ? 'COMPLET' : `${placesRestantes} places restantes`}
                  </p>
                </Link>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}

export default EventList;
