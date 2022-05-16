# FRONTEND/WEBAPP

## Overview
The webapp is built using React, an open-source JavaScript Library, with Kepler.gl and CanvasJS for data visualisation. 
The webapp is able to display bar chart showing the number of tweets related to scenario A and B in each LGA. The website is also able to display a map visualisation of Data from AURIN in a form of heatmap as well as Twitter data in a form of cluster.

## How to run 
### With Docker
1.  Build Docker image - ```docker build -t webapp:latest .```
2.  Run Docker Container - ```docker run -p 3000:3000 -it webapp:latest```
3.  The website should be accessible at http://localhost:3000

### Without Docker
1. ```yarn```
2. ```npm start```
3. The website should be accessible at http://localhost:3000

## Folder Structure 
```
.
├── Dockerfile
├── config-overrides.js
├── docker-compose.yml
├── gulpfile.js
├── jsconfig.json
├── package-lock.json
├── package.json
├── public
│   ├── apple-icon.png
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   └── robots.txt
├── src
│   ├── assets
│   ├── components
│   ├── data
│   ├── index.js
│   ├── layouts
│   ├── routes.js
│   ├── serviceWorker.js
│   ├── setupTests.js
│   └── views
└── yarn.lock
```

### Directories:
- `public` - Contain index.html to intially run the webapp
- `src` - Contain all the source code of the React webapp



