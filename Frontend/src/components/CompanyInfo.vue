<script setup>
import {Card, IftaLabel, InputText, InputMask, Button} from 'primevue';
import ProfileTitle from "@/components/ProfileTitle.vue";
import {ref} from "vue";

const company = ref({
  name: 'БЧ',
  phone: '89132321232',
  inn: '124321234124'
})
</script>

<template>
<div class="company-info">
  <profile-title>Информация о перевозчике</profile-title>
  <Card>
    <template #title>
      Укажите информацию
    </template>
    <template #content>
      <div class="data">
        <IftaLabel>
          <label for="username">Название компании</label>
          <InputText id="name" v-model="company.name" />
        </IftaLabel>
        <IftaLabel>
          <label for="phone">Номер телефона</label>
          <InputMask mask="9-999-999-99-99" id="phone" v-model="company.phone" />
        </IftaLabel>
        <IftaLabel>
          <label for="username">ИНН</label>
          <InputText id="inn" v-model="company.inn" />
        </IftaLabel>
      </div>

      <Button label="Сохранить" style="margin-top: 20px;"></Button>
    </template>
  </Card>
</div>
</template>

<style scoped>
.company-info {
  width: 100%;
}

.data {
  display: flex;
  gap: 20px;
}
</style>