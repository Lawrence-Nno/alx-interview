#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie
 * The first positional argument passed is the Movie ID
 * Display one character name per line in the same order
 * as  list in the /films/ endpoint
 */

const request = require('request');
const filmNumber = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// Makes the API request, sets async to allow await promise
request(filmURL + filmNumber, async (err, res, body) => {
  if (err) return console.error(err);

  // Finds the URLs of each character in the film as a list obj
  const charURLList = JSON.parse(body).characters;

  // Uses the URL list to character pages to make new requests
  // Awaits the queues requests until they resolve in order
  for (const charURL of charURLList) {
    await new Promise((resolve, reject) => {
      request(charURL, (err, res, body) => {
        if (err) return console.error(err);

        // Finds each character's name and prints in URL order
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
