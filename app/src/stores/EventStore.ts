import { defineStore } from 'pinia'
import EventService from '../services/EventService.js'
import { EventItem } from '../types.js'

export const useEventStore = defineStore('EventStore', {
  state() {
    return {
      events: [] as EventItem[],
      event: {} as EventItem
    }
  },
  getters: {
    numberOfEvents: state => state.events.length
  },
  actions: {
    fetchEvents() {
      return EventService.getEvents()
        .then(response => {
          this.events = response.data
        })
        .catch(error => {
          throw error
        })
    },
    createEvent(event: EventItem) {
      return EventService.postEvent(event)
        .then(() => {
          this.events.push(event)
        })
        .catch(error => {
          throw error
        })
    },
    fetchEvent(id: number) {
      return EventService.getEvent(id)
        .then(response => {
          this.event = response.data
        })
        .catch(error => {
          throw error
        })
    },
  }
})