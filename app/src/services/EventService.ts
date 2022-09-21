import axios from 'axios'
import { EventItem, GetEventResponse, GetEventsResponse, CreateEventResponse } from '../types.js'
import { setupInterceptorsTo } from "../plugins/interceptors"

const apiClient = setupInterceptorsTo(axios.create({
  baseURL: 'http://localhost:8002',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
}))

export default {
  getEvents() {
    return apiClient.get<GetEventsResponse>('/events')
  },
  getEvent(id: number) {
    return apiClient.get<GetEventResponse>('/events/' + id)
  },
  postEvent(event: EventItem) {
    return apiClient.post<CreateEventResponse>('/events', event)
  },
  getUserEvents() {
    return apiClient.get<GetEventsResponse>('/users/me/events')
  },
}
