<script setup>
import {FloatLabel} from "primevue";
import {InputText} from "primevue";
import {Password} from "primevue";
import {Button} from "primevue";
import {ref} from "vue";
import {useRouter} from "vue-router";
import {useStore} from "vuex";

const router = useRouter()
const store = useStore()

const user = ref({
  login: null,
  password: null
});

function login() {
  store.state.auth.user = user.value.login || 'Пользователь'

  if (user.value.login === 'admin') {
    store.state.auth.role = 2
  }

  if (user.value.login === 'company') {
    store.state.auth.role = 3
  }

  router.push('/profile')
}
</script>

<template>
<div class="login">
  <div class="login-form">
    <div class="title">
      Авторизация
    </div>
    <FloatLabel>
      <InputText id="username" v-model="user.login" />
      <label for="username">Имя пользователя</label>
    </FloatLabel>
    <FloatLabel style="margin-top: 30px;">
      <Password v-model="user.password" />
      <label for="username">Имя пользователя</label>
    </FloatLabel>
    <Button label="Войти" style="margin-top: 30px; width: 100%" @click="login" />
  </div>
</div>
</template>

<style scoped>
  .login {
    width: 100%;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;

  }

  .login-form .title {
    font-size: 20px;
    font-weight: 600;
    letter-spacing: 2px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 50px;
  }

  .login-form {
    background-color: #fff;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.05);
  }
</style>