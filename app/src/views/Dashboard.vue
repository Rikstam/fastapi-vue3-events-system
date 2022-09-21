<script setup lang="ts">
    import { useEventStore } from '../stores/EventStore'
    import { onBeforeMount, ref } from 'vue'
    import { useRouter } from 'vue-router'
    
    import EventCard from '../components/EventCard.vue';
    import EventService from '../services/EventService'
    
    const eventStore = useEventStore()
    const router = useRouter()
    const isLoading = ref(false)
    const events = ref([])
    
    onBeforeMount(async ()=> {
      isLoading.value = true
      try {
        const response = await EventService.getUserEvents()
        events.value = response.data
      } catch(error) {
        router.push({
          name: 'ErrorDisplay',
          params: { error: `${error}` }
        })
      }
      isLoading.value = false
    })
    </script>
    
    <template>
      <template v-if="isLoading">
        <p>Loading events</p>
      </template>
      <h1>Your events</h1>
      <div class="events">
        <EventCard v-for="event in events" :key="event.id" :event="event" />
      </div>
    </template>
    
    <style scoped>
    .events {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    </style>
    