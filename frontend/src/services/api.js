import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

export const getEvents = async (search = '') => {
  const response = await axios.get(`${API_URL}/events`, {
    params: { search }
  });
  return response.data;
};

export const getEvent = async (id) => {
  const response = await axios.get(`${API_URL}/events/${id}`);
  return response.data;
};

export const getEventRegistrations = async (id) => {
  const response = await axios.get(`${API_URL}/events/${id}/registrations`);
  return response.data;
};

export const createEvent = async (data) => {
  const response = await axios.post(`${API_URL}/events`, data);
  return response.data;
};

export const registerToEvent = async (eventId, data) => {
  const response = await axios.post(`${API_URL}/events/${eventId}/register`, data);
  return response.data;
};
