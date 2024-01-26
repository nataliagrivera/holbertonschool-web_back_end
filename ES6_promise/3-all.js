import { uploadPhoto, createUser } from './utils.js';

function handleProfileSignup() {
  const promises = [uploadPhoto(), createUser()];

  Promise.all(promises)
    .then(([photo, user]) => {
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}

export default handleProfileSignup;
