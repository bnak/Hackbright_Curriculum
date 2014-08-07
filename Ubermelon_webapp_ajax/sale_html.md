#Detailed instructions for the sale banner

## HTML

To make the promotional banner, we need the 'blackout screen', and inside it, the 'jumbotron'.
The HTML for this is very simple, a div nested in another div:

    <div id="blackout-screen">
        <div id="promotion" class="jumbotron">
            <h1>Save on Watermelons! All watermelons 50% off!</h1>
            <a href="" id="close-promotion">Close this window</a>
        </div>
    </div>

Notice that the `<a>` tag doesn't link to anywhere.

Add this HTML at the bottom of your `melon_details` page.
## CSS
The CSS is a little bit tricky, we start by covering the entire window with the blackout screen.

As you enter this style, reload the page after each attribute to see how they affect positioning of items.

    div#blackout-screen {
        background-color: rgba(64, 64, 64, 0.5);
        width: 100%;
        height: 100%;
        position: fixed;
        top: 0px;
        left: 0px;
    }
    
As you inspect your handiwork, make sure you scroll to the bottom of the page to see how the div is being affected.

Here's the css for the 'promotion' div.

    div#promotion {
        width: 600px;
        position: fixed;
        top: 100px;
        left: 50%;
        margin-left: -300px;
    }
    
Lastly, to make our H1 tag _red_, use the following style.

    div#blackout-screen h1 {
        color: red;
    }
