<script setup>
import Navigation from "@/components/Navigation.vue";
import {Card} from "primevue";
import {ref} from "vue";
import {Button} from "primevue";

const selected = ref([]);
const count = Math.random() > 0.5 ? Math.round(Math.random() * 100) : 0
</script>

<template>
<div class="ticket-page">
  <navigation />

  <Card style="width: 25rem; margin-top: 30px; overflow: hidden" class="ticket-card" @click="router.push('/ticket')">
    <template #title>
      <i class="ri-plane-line"></i>
      Минск - Брест
    </template>
    <template #subtitle>
      <b style="margin-bottom: 10px; font-size: 18px;">#7321 | 20.10.2025</b>
      2ч 45м · прямой
      <br><br>
      Количество мест: {{ count }}</template>
    <template #content>
      <div class="cost">
        11 233 ₽
      </div>
    </template>
  </Card>

  <Card style="margin-top: 20px">
    <template #title>
      Укажите посажиров
    </template>
    <template #content>
      <div class="select-tickets">
        <Card style="width: 390px;
              overflow: hidden"
              v-for="i in 6" :key="i"
              class="ticket-item"
              :class="{ active: selected.includes(i) }"
              @click="selected.includes(i) ? selected = selected.filter(item => item !== i) : selected.push(i)"
        >
          <template #title>
            <i class="ri-profile-line"></i>
            Профиль {{ i }}
          </template>
          <template #subtitle>+7 913 232 23 10</template>
          <template #content>
            Иванов Иван Иванович<br>
            10.10.1910<br>
            <div class="passport">
              <span>Выбрать</span>
              <span>Изменить</span>
            </div>
          </template>
        </Card>
      </div>
    </template>
  </Card>

  <Button label="Оформить билет" size="large" style="margin-top: 30px;" :disabled="count === 0" />
</div>
</template>

<style scoped>
.ticket-page {
  padding-bottom: 50px;
}

.select-tickets {
  display: flex;
  gap: 20px;
  justify-content: space-between;
  flex-wrap: wrap;
}

.ticket-item {
  cursor: pointer;
  transition: ease-in-out 0.2s;
  border: 1px solid transparent;
}

.ticket-item.active {
  border: 1px solid var(--p-button-primary-hover-background);
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


.passport {
  display: flex;
  gap: 5px;
  margin-top: 10px;
}
.passport span {
  background-color: var(--p-button-primary-hover-background);
  color: #fff;
  font-size: 18px;
  padding: 5px 10px;
  border-radius: 15px;
}
</style>