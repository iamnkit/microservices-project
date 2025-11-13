# Use official Node.js LTS image
FROM node:20-alpine

# Set working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json first for caching
COPY package*.json ./

# Install dependencies
RUN npm install --production

# Copy the rest of the application code
COPY . .

# Expose the port that Express listens on
EXPOSE 3000

# Set environment variable (optional, for production)
ENV NODE_ENV=production

# Start the API Gateway
CMD ["node", "index.js"]
