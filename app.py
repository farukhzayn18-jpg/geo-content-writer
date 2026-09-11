import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="CreatorKit AI - All-in-One Suite",
    page_icon="🚀",
    layout="wide"
)

# Sidebar (Pricing & Navigation)
st.sidebar.title("🚀 CreatorKit AI")
st.sidebar.info("Replace 5+ expensive tools with one powerful AI suite for just **$29/month**!")

# Subscription Box
st.sidebar.markdown("---")
st.sidebar.subheader("💎 Pro Subscription")
st.sidebar.write("Get access to all tools for **$29/mo** (Save $400+/mo)")
if st.sidebar.button("Upgrade to Pro Now"):
    st.sidebar.success("Redirecting to secure checkout...")

st.sidebar.markdown("---")
menu = st.sidebar.selectbox(
    "Choose Your Tool:",
    [
        "🏠 Dashboard Overview", 
        "📱 Bio Link & Store", 
        "✍️ AI Content & SEO Generator", 
        "💬 Social Media Auto-DM", 
        "📅 Calendar & Bookings"
    ]
)

# Main Dashboard
if menu == "🏠 Dashboard Overview":
    st.title("🔥 Welcome to CreatorKit AI (All-in-One Suite)")
    st.write("Everything you need to grow your business, generate content, and automate tasks in one place—without paying for 5 different apps.")
    
    # Metrics Cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Active Tools Included", value="5+ Powerful Apps", delta="All-in-One")
    with col2:
        st.metric(label="Monthly Cost", value="$29 / mo", delta="Instead of $443")
    with col3:
        st.metric(label="User Satisfaction", value="99.9%", delta="High Speed")

    st.markdown("---")
    st.subheader("What's Included in Your $29/mo Bundle:")
    st.markdown("""
    * 📱 **Mobile Optimized Link-in-Bio Store** (Replaces Linktree & Squarespace)
    * ✍️ **AI Content & SEO Writer** (Generate high-ranking articles & posts instantly)
    * 💬 **Social Media Auto-DMs** (Automate engagement like ManyChat)
    * 📅 **Calendar Invites & Bookings** (Manage client meetings seamlessly)
    * 📊 **Audience Analytics & Email Tools** (Track and grow your audience)
    """)

elif menu == "📱 Bio Link & Store":
    st.title("📱 Mobile Optimized Link-in-Bio Store")
    st.write("Create your stunning landing page and digital store in seconds.")
    
    store_title = st.text_input("Store Name / Brand Title", "My Digital Store")
    bio_text = st.text_area("Bio Description", "Welcome to my official hub! Check out my products below.")
    product_link = st.text_input("Add Product or Social Link", "https://example.com")
    
    if st.button("Publish Bio Store"):
        st.success(f"Your store '{store_title}' is now live and mobile-optimized!")

elif menu == "✍️ AI Content & SEO Generator":
    st.title("✍️ AI Content & SEO Writer")
    st.write("Generate professional blog posts, meta tags, and marketing copies instantly.")
    
    topic = st.text_input("Enter your topic or keyword:", "Best Side Hustles 2026")
    if st.button("Generate Content"):
        with st.spinner("Generating high-quality content..."):
            st.success("Here is your generated content:")
            st.write(f"### Article Title: {topic}")
            st.write(f"This is a high-converting, SEO-optimized piece of content generated automatically for **{topic}**.")

elif menu == "💬 Social Media Auto-DM":
    st.title("💬 Social Media Auto-DMs")
    st.write("Automatically reply to comments and send direct messages to your followers.")
    
    keyword = st.text_input("Trigger Keyword (e.g., 'INFO')", "PRICE")
    reply_message = st.text_area("Automated DM Response", "Thanks for your interest! Here is the link: https://example.com")
    
    if st.button("Save Automation Rule"):
        st.success("Auto-DM rule successfully activated!")

elif menu == "📅 Calendar & Bookings":
    st.title("📅 Calendar Invites & Bookings")
    st.write("Allow clients to book calls or sessions with you automatically.")
    
    st.info("Your booking link: `https://your-app.streamlit.app/book`")
    col1, col2 = st.columns(2)
    with col1:
        st.date_input("Select Available Date")
    with col2:
        st.time_input("Select Available Time")
        
    if st.button("Confirm Booking Slot"):
        st.success("Booking slot successfully configured!")
