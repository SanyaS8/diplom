<script setup>
import { Card } from "primevue";
import {ref} from "vue";
import ProfileTitle from "@/components/ProfileTitle.vue";

const visible = ref(false);
const profile = ref({
  phone: null,
  series: null,
  number: null
});
</script>

<template>
  <div class="profile-tickets">
    <profile-title>Ваши билеты</profile-title>
    <div class="profiles-cards">
      <Card style="width: 30rem; overflow: hidden" class="ticket-card" @click="router.push('/ticket')" v-for="i in 5" :key="i">
        <template #title>
          <i class="ri-plane-line"></i>
          Минск - Брест
        </template>
        <template #subtitle>
          <b style="margin-bottom: 10px; font-size: 18px;">#7321 | 20.10.2025</b>
          2ч 45м · прямой</template>
        <template #content>
          <div class="cost">
            Отменить
          </div>

          <div class="warn" v-if="i % 3 === 0">
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