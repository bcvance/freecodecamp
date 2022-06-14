document.addEventListener("DOMContentLoaded", () => {
    // pagination
    let posts = document.getElementsByClassName("post-edit-container");
    for (let i=0; i<posts.length; i++) {
        if (i<10) {
            posts[i].style.display = "block";
        }
        else {
            posts[i].style.display = "none";
        }
        
    }

    document.addEventListener("click", (event) => {
        // if user clicked on like icon
        if (event.target.className === "like-icon"){
            let thumbs_up;
            let numLikes;
            let isLiked;
            let parent = event.target.parentNode;
            let children = parent.childNodes;
            // iterating through child nodes and saving their elements in variables
            for (let i=0; i<children.length; i++){
                if (children[i].tagName == "img"){
                    thumbs_up = children[i];
                }
                else if (children[i].className == "num-likes") {
                    numLikes = children[i];
                }
                else if (children[i].className == "is-liked"){
                    isLiked = children[i];
                }
            }
            // if post not liked, make appropriate changes to HTML
            if (isLiked.innerHTML === "Not Liked"){
                numLikes.innerHTML ++;
                isLiked.innerHTML = "Liked";
            }
            // and vice versa if it is liked
            else {
                numLikes.innerHTML --;
                isLiked.innerHTML = "Not Liked";
            }
            // request to url which triggers like function in views.py
            const postId = parent.dataset.postId;
            fetch(`/like/${postId}`)
        }
    })

    let editBtns = document.getElementsByClassName("edit")
    for (let i=0; i<editBtns.length; i++) {
        let content;
        editBtns[i].onclick = (event) => {
            let postId = event.target.parentNode.dataset.postId;
            const postEditContainers = document.getElementsByClassName("post-edit-container");
            for (j=0; j<postEditContainers.length; j++) {
                if (postEditContainers[j].dataset.postId !== postId) {
                    // console.log(postEditContainers[j].childNodes);
                    postEditContainers[j].childNodes[1].style.display = "block";
                    postEditContainers[j].childNodes[3].style.display = "none";
                }
                else {
                    // console.log(postEditContainers[j].childNodes);
                    postEditContainers[j].childNodes[1].style.display = "none";
                    postEditContainers[j].childNodes[3].style.display = "block";
                }
            }
            // getting the edit card element so I can make its submit button child functional
            let editCard = document.getElementById(`edit-card-${postId}`);
            let editedContent = editCard.childNodes[3];
            let saveBtn = editCard.childNodes[5];
            let closeBtn = editCard.childNodes[1];
            closeBtn.onclick = () => {
                document.getElementById(`post-card-${postId}`).style.display = "block";
                editCard.style.display = "none";
            }
            // make async call to server when save button is clicked
            saveBtn.onclick = () => {
                fetch(`edit/${editCard.dataset.postId}`, {
                    method: "PUT",
                    body: JSON.stringify({
                        content: editedContent.value
                    })
                })
                let postCard = document.getElementById(`post-card-${postId}`);
                console.log(postCard.childNodes[3]);
                let postContent = postCard.childNodes[3];
                postContent.innerHTML = editedContent.value; 
                editedContent.innerHTML = ""; 
                editCard.style.display = "none";
                postCard.style.display = "block";
            }
            // for (let j=0; j<saveBtns.length; j++){
            //     saveBtns[j].onclick = (event) => {
            //         console.log(document.getElementById("editpost").innerHTML);
            //         fetch(`edit/${event.target.parentNode.dataset.postId}`, {
            //         method: "PUT",
            //         body: JSON.stringify({
            //             content: document.getElementById("editpost").innerHTML
            //         })
            //     });
            //     }
            // }
            }
        } 

    // adding event listeners to pagination buttons to show the correct range of posts
    let body = document.querySelector("div.body");
    if (body.childNodes[1].dataset.title === "index" || body.childNodes[1].dataset.title === "following") {
        let pageBtns = document.getElementsByClassName("page-number");
        pageBtns[0].style.fontWeight = "bold";
        for (let i=0; i<pageBtns.length; i++) {
            pageBtns[i].onclick = (event) => {
                for (let t=0; t<pageBtns.length; t++) {
                    pageBtns[t].style.fontWeight = "normal";
                }
                event.target.style.fontWeight = "bold";
                let pageNumber = event.target.dataset.pageNumber;
                for (let j=0; j<posts.length; j++) {
                    if (j < 10*(pageNumber-1) || j > 10*(pageNumber)-1) {
                        posts[j].style.display = "none";
                    }
                    else {
                        posts[j].style.display = "block";
                    }
                }
            }
        }
    } 

    if (body.childNodes[1].dataset.title === "profile") {
        document.getElementById("followers").onclick = () => {
            document.getElementById("post-section").style.display = "none";
            document.getElementById("followers-section").style.display = "block";
            document.getElementById("following-section").style.display = "none";
            document.getElementById("liked-section").style.display = "none";
        }
        document.getElementById("following").onclick = () => {
            document.getElementById("post-section").style.display = "none";
            document.getElementById("followers-section").style.display = "none";
            document.getElementById("following-section").style.display = "block";
            document.getElementById("liked-section").style.display = "none";
        }
        document.getElementById("liked").onclick = () => {
            document.getElementById("post-section").style.display = "none";
            document.getElementById("followers-section").style.display = "none";
            document.getElementById("following-section").style.display = "none";
            document.getElementById("liked-section").style.display = "block";
        }
        document.getElementById("posts").onclick = () => {
            document.getElementById("post-section").style.display = "block";
            document.getElementById("followers-section").style.display = "none";
            document.getElementById("following-section").style.display = "none";
            document.getElementById("liked-section").style.display = "none";
        }
    
        let followBtn = document.getElementById("follow-btn");
        followBtn.onclick = () => {
            if (followBtn.innerHTML === "Follow") {
                followBtn.innerHTML = "Unfollow";
                document.getElementById("num-followers").innerHTML ++;
            }
            else {
                followBtn.innerHTML = "Follow";
                document.getElementById("num-followers").innerHTML --;
            }
            url = `/follow/${followBtn.dataset.userId}`
            fetch(url)
        }
    }
    
})