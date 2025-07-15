
let likes=7;
let isLiked=false;


if(!isLiked){
 document.querySelector(".like-icon").innerHTML = `<i class="fa-regular fa-heart"></i> ${likes}`
}else{
  document.querySelector(".like-icon").innerHTML = `<i class="fa-regular fa-heart"></i> ${likes}`
}


function toggleLike() {
 element= document.querySelector(".like-icon")
  element.innerHTML = `<i class="fa-regular fa-heart"></i> ${likes}`
  if (isLiked) {
    likes--;
    element.innerHTML = `<i class="fa-regular fa-heart"></i> ${likes}`;  // Unliked
    isLiked=false;
    element.classList.remove("liked");
    // Optional: send "unlike" to server
    // sendLikeStatus(movieId, false);
  } else {
    likes++;
    element.innerHTML = `<i class="fa-solid fa-heart" style="color:red"></i> ${likes}`;  // Liked
    isLiked = "true";
    element.classList.add("liked");
    

   
    // Optional: send "like" to server
    // sendLikeStatus(movieId, true);
  }
}

