import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  base: '/PROYECTOS/Desarrollo_web/react1/desarrollo-web/', // Ruta base para GitHub Pages
  plugins: [react()],
  build: {
    outDir: 'build', // Directorio de salida
  },
});