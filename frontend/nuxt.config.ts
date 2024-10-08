// https://nuxt.com/docs/api/configuration/nuxt-config
import { config } from 'dotenv';

config({ path: '../.env' });

export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  runtimeConfig: {
    public: {},
  },
});
