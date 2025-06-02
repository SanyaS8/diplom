<script setup>
import {Card} from "primevue";
import {useRouter} from "vue-router";

const router = useRouter()
</script>

<template>
 <div class="ticket-list">
   <Card style="width: 25rem; overflow: hidden" v-for="i in 12" :key="i" class="ticket-card" @click="router.push('/ticket')">
     <template #title>
       <i class="ri-plane-line"></i>
       Минск - Брест
     </template>
     <template #subtitle>
       <b style="margin-bottom: 10px; font-size: 18px;">#7321 | 20.10.2025</b>
       <br>
       2ч 45м · прямой
      <br><br>
       Количество мест: {{ i * 3}}
     </template>
     <template #content>
       <div class="cost">
         11 233 ₽
       </div>
     </template>
   </Card>
 </div>
</template>

<style scoped>
.ticket-list {
  margin-top: 50px;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: space-between;
}

.ticket-list .cost {
  background-color: var(--p-button-primary-hover-background);
  display: inline-flex;
  color: #fff;
  padding: 10px 15px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 50px;
}

.ticket-card {
  cursor: pointer;
  transition: ease-in-out 0.2s;

  &:hover {
    box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.1);
  }
}
</style>