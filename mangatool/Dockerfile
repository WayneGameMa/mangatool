# Stage 1: Build the Quasar app
FROM node as build

# Set the working directory inside the container
WORKDIR /app

# Install Quasar CLI globally
RUN npm install -g @quasar/cli
RUN npm install @fortawesome/fontawesome-free


COPY . .

# Install dependencies
RUN npm install


# Build the Quasar app
RUN quasar build

# Stage 2: Serve the built app using Nginx
FROM nginx

# Remove the default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy the Nginx configuration for the Quasar app to the container
COPY nginx.conf /etc/nginx/conf.d

# Copy the built Quasar app from the previous stage to the Nginx web root directory
COPY --from=build /app/dist/spa /usr/share/nginx/html

# Expose port 80 to access the app
EXPOSE 80