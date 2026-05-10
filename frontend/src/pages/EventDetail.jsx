import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { getEvent, getEventRegistrations, registerToEvent } from '../services/api';

function EventDetail() {
  const { id } = useParams();
  const [event, setEvent] = useState(null);
  const [registrations, setRegistrations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    email: ''
  });
  const [message, setMessage] = useState(null);

  useEffect(() => {
    loadEvent();
  }, [id]);

  const loadEvent = async () => {
    try {
      const [eventData, registrationsData] = await Promise.all([
        getEvent(id),
        getEventRegistrations(id)
      ]);
      setEvent(eventData);
      setRegistrations(registrationsData);
    } catch (error) {
      console.error('Erreur:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await registerToEvent(id, formData);
      setMessage({ type: 'success', text: 'Inscription réussie !' });
      setFormData({ first_name: '', last_name: '', email: '' });
      loadEvent();
    } catch (error) {
      const errorMsg = error.response?.data?.detail?.message || 'Erreur lors de l\'inscription';
      setMessage({ type: 'error', text: errorMsg });
    }
  };

  if (loading) return <p className="p-8">Chargement...</p>;
  if (!event) return <p className="p-8">Événement non trouvé</p>;

  const placesRestantes = event.capacity - registrations.length;
  const isComplet = placesRestantes === 0;

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-2xl mx-auto px-4 py-8">
        <Link to="/" className="text-blue-600 hover:underline mb-4 block">
          ← Retour à la liste
        </Link>

        <div className="bg-white p-6 rounded-lg shadow mb-6">
          <h1 className="text-3xl font-bold mb-4">{event.title}</h1>
          <p className="text-gray-700 mb-2">{event.description}</p>
          <p className="text-gray-600">{new Date(event.date).toLocaleString('fr-FR')}</p>
          <p className="text-gray-600">{event.location}</p>
          <p className={`mt-4 text-lg font-semibold ${isComplet ? 'text-red-600' : 'text-green-600'}`}>
            {placesRestantes} places restantes sur {event.capacity}
          </p>
        </div>

        {isComplet ? (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
            Cet événement est complet.
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-xl font-bold mb-4">S'inscrire</h2>
            
            <input
              type="text"
              placeholder="Prénom"
              value={formData.first_name}
              onChange={(e) => setFormData({ ...formData, first_name: e.target.value })}
              required
              className="w-full px-4 py-2 border rounded mb-3"
            />
            
            <input
              type="text"
              placeholder="Nom"
              value={formData.last_name}
              onChange={(e) => setFormData({ ...formData, last_name: e.target.value })}
              required
              className="w-full px-4 py-2 border rounded mb-3"
            />
            
            <input
              type="email"
              placeholder="Email"
              value={formData.email}
              onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              required
              className="w-full px-4 py-2 border rounded mb-4"
            />
            
            <button
              type="submit"
              className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
            >
              S'inscrire
            </button>
          </form>
        )}

        {message && (
          <div className={`mt-4 p-4 rounded ${
            message.type === 'success' ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'
          }`}>
            {message.text}
          </div>
        )}
      </div>
    </div>
  );
}

export default EventDetail;
