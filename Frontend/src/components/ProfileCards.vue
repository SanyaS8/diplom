<script setup>

import {Button, Card, DatePicker, InputMask, InputText} from "primevue";
import Dialog from "primevue/dialog";
import {ref} from "vue";
import ProfileTitle from "@/components/ProfileTitle.vue";

const visible = ref(false);
const profile = ref({
  phone: null,
  series: null,
  number: null
});

const profiles = ref([
  { id: 1, name: "Иванов Иван Иванович", phone: "+375 29 123-45-67", birthDate: "10.10.1990" },
  { id: 2, name: "Петров Петр Петрович", phone: "+375 29 234-56-78", birthDate: "15.05.1985" },
  { id: 3, name: "Сидоров Сидор Сидорович", phone: "+375 29 345-67-89", birthDate: "20.08.1978" },
  { id: 4, name: "Смирнов Сергей Сергеевич", phone: "+375 29 456-78-90", birthDate: "25.12.1992" },
  { id: 5, name: "Васильев Василий Васильевич", phone: "+375 29 567-89-01", birthDate: "05.07.1980" }
]);
</script>

<template>
  <div class="profile-tickets">
    <profile-title>Ваши профили</profile-title>
    <div class="profiles-cards">
      <Card style="width: 30rem; overflow: hidden" v-for="profile in profiles" :key="profile.id">
        <template #title>
          <i class="ri-profile-line"></i>
          Профиль {{ profile.id }}
        </template>
        <template #subtitle>{{ profile.phone }}</template>
        <template #content>
          {{ profile.name }}<br>
          {{ profile.birthDate }}<br>
          <div class="passport">
            <span>Изменить</span>
            <span>Удалить</span>
          </div>
        </template>
      </Card>
      <Card style="width: 30rem; overflow: hidden">
        <template #title>
          <i class="ri-add-box-line"></i>
          Новый профиль
        </template>
        <template #content>
          <div class="create-profile">
            <Button label="Создать" style="margin-top: 20px" @click="visible = true" />
          </div>
        </template>
      </Card>
    </div>

    <div class="card flex justify-center">
      <Dialog v-model:visible="visible" modal header="Создание профиля" :style="{ width: '25rem' }">
        <span style="display: block; margin-bottom: 40px">Укажите нужную информацию</span>
        <div style="display: flex; justify-content: space-between; align-items: center">
          <label for="name" style="font-weight: 600">ФИО</label>
          <InputText id="name" v-model="profile.name" placeholder="Иванов Иван Иванович" />
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 20px;">
          <label for="phone" style="font-weight: 600">Телефон</label>
          <InputMask id="phone" v-model="profile.phone" mask="9-999-999-99-99" placeholder="8-900-000-00-00" />
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 20px;">
          <label for="date" style="font-weight: 600">Дата рождения</label>
          <DatePicker format="dd.mm.yy" placeholder="Укажите дату рождения" />
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 20px; align-items: center">
          <label for="series" style="font-weight: 600">Серия паспорта</label>
          <InputMask id="series" v-model="profile.series" mask="99-99" placeholder="00-00" />
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 20px; align-items: center">
          <label for="number" style="font-weight: 600">Номер паспорта</label>
          <InputMask id="number" v-model="profile.number" mask="999999" placeholder="000000" />
        </div>
        <div style="margin-top: 30px; display: flex; gap: 10px;">
          <Button type="button" label="Отмена" severity="secondary" @click="visible = false"></Button>
          <Button type="button" label="Сохранить" @click="visible = false"></Button>
        </div>
      </Dialog>
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