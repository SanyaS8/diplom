<script setup>
import { Card } from "primevue";
import { ref } from "vue";
import ProfileTitle from "@/components/ProfileTitle.vue";

const tickets = ref([
  { id: 1, route: "Минск - Брест", number: "7321", date: "20.10.2025", duration: "2ч 45м", type: "прямой", cost: "15.50", cancelled: false },
  { id: 2, route: "Минск - Гродно", number: "8452", date: "21.10.2025", duration: "3ч 10м", type: "прямой", cost: "18.00", cancelled: true },
  { id: 3, route: "Минск - Витебск", number: "9123", date: "22.10.2025", duration: "4ч 20м", type: "с пересадкой", cost: "20.00", cancelled: false },
  { id: 4, route: "Минск - Гомель", number: "4567", date: "23.10.2025", duration: "3ч 50м", type: "прямой", cost: "17.80", cancelled: false },
  { id: 5, route: "Минск - Могилев", number: "6789", date: "24.10.2025", duration: "2ч 30м", type: "прямой", cost: "14.00", cancelled: true }
]);
</script>

<template>
  <div class="profile-tickets">
    <profile-title>Ваши билеты</profile-title>
    <div class="profiles-cards">
      <Card style="width: 30rem; overflow: hidden" class="ticket-card" @click="router.push('/ticket?id=1')" v-for="ticket in tickets" :key="ticket.id">
        <template #title>
          <i class="ri-train-line"></i>
          {{ ticket.route }}
        </template>
        <template #subtitle>
          <b style="margin-bottom: 10px; font-size: 18px;">#{{ ticket.number }} | {{ ticket.date }}</b>
          {{ ticket.duration }} · {{ ticket.type }}</template>
        <template #content>
          <div class="cost">
            {{ ticket.cost }} BYN
          </div>

          <div class="warn" v-if="ticket.cancelled">
            <i class="ri-error-warning-line"></i>
            Перевозчик отменил рейс
          </div>
        </template>
      </Card>
    </div>
  </div>
</template>

<style scoped>
.profile-tickets {
  margin-bottom: 50px;
}
.profiles-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: space-between;
  font-size: 18px;
}

.ticket-card .cost {
  background-color: var(--p-button-primary-hover-background);
  display: inline-flex;
  color: #fff;
  padding: 10px 15px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 50px;
}

.ticket-card .warn {
  background-color: #b7b700;
  display: inline-flex;
  color: #fff;
  padding: 10px 15px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 50px;
  align-items: center;
  gap: 10px;
  margin-left: 10px;
}
</style>