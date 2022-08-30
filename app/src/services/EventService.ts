import axios from 'axios'
import { EventItem } from '../types.js'


type GetEventsResponse = {
  data: EventItem[]
}

type GetEventResponse = {
  data: EventItem
}

type CreateEventResponse = {
  data: EventItem
}

const apiClient = axios.create({
  baseURL: 'http://localhost:8002',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
})

export default {
  getEvents() {
    return apiClient.get<GetEventsResponse>('/events')
  },
  getEvent(id: number) {
    return apiClient.get<GetEventResponse>('/events/' + id)
  },
  postEvent(event: EventItem) {
    return apiClient.post<CreateEventResponse>('/events', event)
  }
}
