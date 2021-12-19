from apps.common.constant import GlobalConstant


class GroceryListStatus(GlobalConstant):
    """
    Constants for Grocery list status
    """
    Active = "active"  # status when list is created and all items yet to be purchased
    Partial = "partial"  # status when some of the items has been already purchased and few are pending
    Completed = "completed"  # status when all items are marked as purchased

    FieldStr = {
        Active: "Active",
        Partial: "Partial",
        Completed: "Completed",
    }


class GroceryItemStatus(GlobalConstant):
    """
    Constants for reminder interval
    """
    Pending = "pending"
    Done = "done"

    FieldStr = {
        Pending: "pending",
        Done:"done"
    }

class ReminderInterval(GlobalConstant):
    """
    Constants for reminder interval
    """
    Daily = "day"
    Weekly = "week"
    Monthly = "month"

    FieldStr = {
        Daily: "day",
        Weekly:"week",
        Monthly: "month",
    }
