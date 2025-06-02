<script setup>
import {Button} from "primevue";
import {useRouter} from "vue-router";
import {useStore} from "vuex";
import ProfileTitle from "@/components/ProfileTitle.vue";

const router = useRouter()
const store = useStore()

function logout() {
  store.state.auth.user = null
  router.push('/')
}
</script>

<template>
  <div class="logout-page">
    <profile-title>Выход из аккаунта</profile-title>
    <div class="logout">
      <div class="title">Вы уверены, что хотите выйти?</div>
      <Button label="Выйти" size="large" @click="logout" />
    </div>
  </div>
</template>

<style scoped>
.logout-page {
  width: 100%;
}
.logout {
  display: flex;
  padding: 30px;
  background-color: #fff;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.title {
  font-size: 32px;
  font-weight: 600;
  margin-bottom: 20px;
}
</style>