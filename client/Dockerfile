FROM node:20-bullseye AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci

FROM node:20-bullseye AS dev
WORKDIR /app
COPY --from=deps /app/node_modules /app/node_modules
COPY . .
CMD ["npm","run","dev","--","--host","0.0.0.0","--port","3000"]

FROM deps AS build
COPY . .
RUN npm run build

FROM node:20-bullseye AS runtime
WORKDIR /app
ENV NODE_ENV=production
COPY package*.json ./
RUN npm ci --omit=dev
COPY --from=build /app/build ./build
EXPOSE 3000
CMD ["node","build"]
